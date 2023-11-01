The authors of the **Automatic Monitoring of Pigs** dataset recognized the significance of animals expressing their internal and external stimuli through behaviour changes, particularly in assessing their health and welfare. They designed an algorithm based on deep learning for detecting and tracking pig posture and locomotion activities. This algorithm aimed to measure behaviour changes in an experimental pig barn under different greenhouse gas (GHG) levels.

The study involved elevating GHG levels in the barn by closing ventilators for specific durations throughout the day and night. Simultaneously, the corresponding pig posture and locomotion activities were observed before, during, and after each treatment. The results indicated that as GHG concentration increased, pig activity levels decreased, resulting in longer durations of lateral-lying posture. Moreover, activities like standing, sternal-lying, and walking decreased as GHG levels rose. This suggested that monitoring and tracking pig physical behaviours through a simple RGB camera and deep learning models could effectively assess individual pig health and welfare.

|        Pig Posture and Label        |                Identification Convention                | Instances |
| :---------------------------------: | :------------------------------------------------------: | :-------: |
| ***standing pig*** (standing_pig) |  Only feet or feet and snout in contact with the floor  |  10,124  |
| ***sternal lying pig*** (sl_pig) |     Belly and folded limbs in contact with the floor     |   9364   |
| ***lateral lying pig*** (ll_pig) | Side trunk and extended limbs in contact with the ground |  10,745  |

The experimental setup took place in a controlled pig barn, with specific conditions (see [details](https://www.mdpi.com/2076-2615/11/11/3089/htm#) in the paper) applied to raise GHG concentrations. The study involved five Yorkshire breed pigs, and their conditions were well-documented, including feeding schedules and markings for visual identification. 

The GHG concentrations were measured using gas chromatography, with carbon dioxide (CO2) being the dominant GHG. The concentrations were analyzed before, after, and one hour after treatment. The authors provided data and graphs illustrating the GHG concentrations of ***CO2_ppm*** and ***CO_NO_CH4_N2O_ppm*** over time.

<img src="https://github.com/supervisely/supervisely/assets/78355358/db98fe61-cbd1-40a8-8a1a-8f4e47521612" alt="image" width="800">

<span style="font-size: smaller; font-style: italic;">Average greenhouse gas (GHG) concentrations before, during, and after an hour of treatment. The x-axis represents the time (hh:mm) of day, whereas the left y-axis represents the average CO2 concentration, and the right y-axis represents the average CO, NO, CH4, and N<sub>2</sub>O.</span>

The study also included group-wise pig posture and walking behaviour ***score***, which were assessed by counting the number of pigs exhibiting specific behaviours in each frame ***before treatment***, ***during treatment***, and ***after treatment***. These scores revealed that pig behaviour was affected by GHG levels, with increased lateral lying and reduced standing and walking activities during elevated GHG conditions.

<img src="https://github.com/supervisely/supervisely/assets/78355358/327a0842-6924-4ad4-b461-9199f961ca6e" alt="image" width="800">

<span style="font-size: smaller; font-style: italic;">Group-wise average posture and walking frame scores of pigs: (a) standing score, (b) walking score, (c) sternal-lying score, and (d) lateral-lying score. The scores show the average number of pigs in a frame with a particular posture. The bars represent the average activity scores obtained in three days at an hour before, during, and after the treatment period in the morning, day, and nighttime.</span>

Additionally, the authors presented locomotion patterns and distances travelled by walking pigs during the experiments. These observations provided insights into how GHG levels influenced pig activities throughout the day.

<img src="https://github.com/supervisely/supervisely/assets/78355358/e29d7cf8-779a-4ed3-acba-024afb029f56" alt="image" width="800">

<span style="font-size: smaller; font-style: italic;">Total distance travelled by the pigs in the group and the day 1-morning time locomotion activities: (a) the total distance travelled by all pigs during the study period, (b) locomotion of the group pigs before treatment in the morning of day 1, (c) during the treatment, and (d) after the treatment.</span>

In summary, the authors conducted a comprehensive study to assess the impact of elevated GHG levels on pig behaviour using computer vision and deep learning techniques. Their findings underscored the potential of this approach for non-invasive monitoring of pig health and welfare under varying environmental conditions.
