#!/bin/bash
#SBATCH --job-name=Convert_Hyburn_Small_Mg
#SBATCH -p scarf
#SBATCH --output=convert-Hyburn_Small_Mg.txt
#SBATCH --ntasks=17
#SBATCH --cpus-per-task=1
#SBATCH --time=23:59:59
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/Mg/test_T_10_0_0.ppf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/Mg/test_T_10_0_1.ppf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/Mg/test_T_10_0_2.ppf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/Mg/test_T_10_1_0.ppf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/Mg/test_T_10_1_1.ppf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/Mg/test_T_10_1_2.ppf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/Mg/test_T_10_2_0.ppf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/Mg/test_T_10_2_1.ppf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/Mg/test_T_10_2_2.ppf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/Mg/test_T_10_3_0.ppf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/Mg/test_T_10_3_1.ppf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/Mg/test_T_10_3_2.ppf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/Mg/test_T_10_4_0.ppf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/Mg/test_T_10_4_1.ppf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/Mg/test_T_10_4_2.ppf
