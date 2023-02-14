#!/bin/bash
#SBATCH --job-name=Hyburn
#SBATCH -p scarf
#SBATCH --output=hyades_output.txt
#SBATCH --ntasks=20
#SBATCH --cpus-per-task=1
#SBATCH --time=23:59:59
hyades -c /home/vol05/scarf1185/icfBurnwave/test/data/scripts/test_6_0.inf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/data/scripts/test_6_1.inf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/data/scripts/test_6_2.inf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/data/scripts/test_6_3.inf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/data/scripts/test_6_4.inf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/data/scripts/test_6_5.inf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/data/scripts/test_6_6.inf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/data/scripts/test_6_7.inf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/data/scripts/test_6_8.inf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/data/scripts/test_6_9.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/data/scripts/test_6_0.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/data/scripts/test_6_1.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/data/scripts/test_6_2.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/data/scripts/test_6_3.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/data/scripts/test_6_4.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/data/scripts/test_6_5.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/data/scripts/test_6_6.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/data/scripts/test_6_7.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/data/scripts/test_6_8.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/data/scripts/test_6_9.inf
