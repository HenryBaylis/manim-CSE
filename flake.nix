{
  inputs.nixpkgs.url = "github:nixos/nixpkgs?ref=25.05";

  outputs = { self, nixpkgs } : let
    system = builtins.currentSystem;
    pkgs = import nixpkgs { inherit system; };
  in {
    devShells.${system}.default = pkgs.mkShell {
      packages = with pkgs; [
        uv
        (pkgs.python3.withPackages (python-pkgs: with python-pkgs; [
          # select Python packages here
          cairosvg
        ]))
        cairo
        sox
        ffmpeg
        cmake
        pkg-config
        texliveFull
      ];
    };
  };
}
