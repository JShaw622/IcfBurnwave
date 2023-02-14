#!/bin/bash
#SBATCH --job-name=Hyburn
#SBATCH -p scarf
#SBATCH --output=hyades_output.txt
#SBATCH --ntasks=200
#SBATCH --cpus-per-task=1
#SBATCH --time=23:59:59
hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_0_0.inf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_0_1.inf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_0_2.inf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_0_3.inf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_0_4.inf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_0_5.inf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_0_6.inf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_0_7.inf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_0_8.inf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_0_9.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/scripts/test_0_0..ppf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/scripts/test_0_1..ppf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/scripts/test_0_2..ppf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/scripts/test_0_3..ppf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/scripts/test_0_4..ppf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/scripts/test_0_5..ppf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/scripts/test_0_6..ppf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/scripts/test_0_7..ppf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/scripts/test_0_8..ppf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/scripts/test_0_9..ppf
