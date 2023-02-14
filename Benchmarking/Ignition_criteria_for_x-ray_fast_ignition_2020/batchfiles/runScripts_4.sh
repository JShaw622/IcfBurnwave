#!/bin/bash
#SBATCH --job-name=Hyburn
#SBATCH -p scarf
#SBATCH --output=hyades_output.txt
#SBATCH --ntasks=20
#SBATCH --cpus-per-task=1
#SBATCH --time=23:59:59
hyades -c /home/vol05/scarf1185/icfBurnwave/test/data/scripts/test_4_0.inf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/data/scripts/test_4_1.inf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/data/scripts/test_4_2.inf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/data/scripts/test_4_3.inf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/data/scripts/test_4_4.inf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/data/scripts/test_4_5.inf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/data/scripts/test_4_6.inf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/data/scripts/test_4_7.inf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/data/scripts/test_4_8.inf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/data/scripts/test_4_9.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/data/scripts/test_4_0.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/data/scripts/test_4_1.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/data/scripts/test_4_2.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/data/scripts/test_4_3.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/data/scripts/test_4_4.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/data/scripts/test_4_5.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/data/scripts/test_4_6.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/data/scripts/test_4_7.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/data/scripts/test_4_8.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/data/scripts/test_4_9.inf
