{ pkgs }: {
  deps = [
    pkgs.python310Packages.wandb
    pkgs.evcc
  ];
}