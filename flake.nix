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
          pkgs.dockerTools.buildLayeredImage {
            name = "telsok";
            tag = "latest";
            created = "now";
            contents = [
              app
              pkgs.chromedriver
              pkgs.chromium
              pkgs.coreutils
              pkgs.util-linux
              pkgs.bash
              poetryEnv
            ];

            # selenium data dir
            # cannot create temp dir for user data dir
            extraCommands = "mkdir -p /tmp";

            config = {
              Cmd = ["python" "telsok.py"];
              Env = [
                "CHROMEDRIVER_PATH=${pkgs.chromedriver + "/bin/chromedriver"}"
                "CHROME_PATH=${pkgs.chromium + "/bin/chromium"}"
              ];
            };
          };

        devShells.default = pkgs.mkShell {
          packages = [
            pkgs.chromedriver
            pkgs.chromium
            pkgs.poetry
            poetryEnv
          ];
          POETRY_VIRTUALENVS_IN_PROJECT = true;
          shellHook = ''
            export CHROMEDRIVER_PATH=${pkgs.chromedriver + "/bin/chromedriver"}
            export CHROME_PATH=${pkgs.chromium + "/bin/chromium"}
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
