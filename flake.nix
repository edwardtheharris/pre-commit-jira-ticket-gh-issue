{
  description = "App Eng env flake";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
    systems.url = "github:nix-systems/default";
  };

  outputs = inputs @ {
    self,
    nixpkgs,
    systems,
  }: let
    forEachSystem = nixpkgs.lib.genAttrs (import systems);
  in {
    devShells =
      forEachSystem
      (
        system: let
          pkgs = nixpkgs.legacyPackages.${system};
        in {
          pre-commit = pkgs.mkShell {
            buildInputs = [
              pkgs.python313
              pkgs.python313Packages.pip
              pkgs.pipenv
              pkgs.pre-commit
            ];
            shellHook = ''
              export PIPENV_VENV_IN_PROJECT=1
              python3 -m pip install -U pip pipenv
              pipenv install
              pipenv shell
              pre-commit install
              pre-commit install-hooks
            '';
          };
          docs = pkgs.mkShell {
            buildInputs = [
              pkgs.python313
              pkgs.python313Packages.pip
              pkgs.pipenv
              pkgs.pre-commit
            ];
            shellHook = ''
              export PIPENV_VENV_IN_PROJECT=1
              python3 -m pip install -U pip pipenv
              pipenv install --dev
              pipenv run sphinx-autobuild -a -b _build/html -E . _build/auto
            '';
          };
        }
      );
    packages =
      forEachSystem
      (
        system: let
          pkgs = nixpkgs.legacyPackages.${system};
        in {
          packages.${system}.pre-commit = nixpkgs.legacyPackages.${system}.pre-commit;
          packages.${system}.default = self.packages.${system}.pre-commit;
        }
      );
  };
}
