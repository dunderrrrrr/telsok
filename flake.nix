{
  inputs = {
    poetry2nix = {
      url = "github:nix-community/poetry2nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
    alejandra = {
      url = "github:kamadorueda/alejandra/3.0.0";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };
  outputs = inputs @ {
    self,
    nixpkgs,
    flake-parts,
    systems,
    poetry2nix,
    alejandra,
    ...
  }:
    flake-parts.lib.mkFlake {inherit inputs;} {
      systems = import systems;
      perSystem = {
        pkgs,
        lib,
        system,
        self',
        ...
      }: let
        poetryEnv = pkgs.callPackage ./. {};
      in {
        _module.args.pkgs = import nixpkgs {
          inherit system;
          overlays = [poetry2nix.overlays.default];
        };

        packages.dockerImage = let
          appPort = "9191";
          app = pkgs.lib.fileset.toSource {
            root = ./.;
            fileset = ./.;
          };
        in
          pkgs.dockerTools.buildImage {
            name = "telsok";
            tag = "latest";
            created = "now";
            copyToRoot = pkgs.buildEnv {
                name = "image-root";
                pathsToLink = ["/"];
                paths = [
                    app
                    # pkgs.coreutils
                    # pkgs.util-linux
                    # pkgs.bash
                    poetryEnv
                ];
            };
            config = {
              Cmd = ["python" "telsok.py"];
            };
          };

        devShells.default = pkgs.mkShell {
          packages = [
            pkgs.poetry
            poetryEnv
          ];
          POETRY_VIRTUALENVS_IN_PROJECT = true;
          shellHook = ''
            export FLASK_APP="telsok"

            ${lib.getExe pkgs.poetry} env use ${lib.getExe pkgs.python3}
            ${lib.getExe pkgs.poetry} install --all-extras --no-root --sync
            set -a
            source .env 2> /dev/null
          '';
        };
      };
    };
}
