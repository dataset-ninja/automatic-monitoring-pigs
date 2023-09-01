The authors of the **Automatic Monitoring of Pigs** dataset recognized the significance of animals expressing their internal and external stimuli through behavior changes, particularly in assessing their health and welfare. They designed an algorithm based on deep learning for detecting and tracking pig posture and locomotion activities. This algorithm aimed to measure behavior changes in an experimental pig barn under different greenhouse gas (GHG) levels.

The study involved elevating GHG levels in the barn by closing ventilators for specific durations throughout the day and night. Simultaneously, the corresponding pig posture and locomotion activities were observed before, during, and after each treatment. The results indicated that as GHG concentration increased, pig activity levels decreased, resulting in longer durations of lateral-lying posture. Moreover, activities like standing, sternal-lying, and walking decreased as GHG levels rose. This suggested that monitoring and tracking pig physical behaviors through a simple RGB camera and deep learning models could effectively assess individual pig health and welfare.

|        Pig Posture and Label        |                Identification Convention                | Instances |
| :---------------------------------: | :------------------------------------------------------: | :-------: |
| ***standing pig*** (standing_pig) |  Only feet or feet and snout in contact with the floor  |  10,124  |
| ***sternal lying pig*** (sl_pig) |     Belly and folded limbs in contact with the floor     |   9364   |
| ***lateral lying pig*** (ll_pig) | Side trunk and extended limbs in contact with the ground |  10,745  |

The experimental setup took place in a controlled pig barn, with specific conditions (see [details](https://www.mdpi.com/2076-2615/11/11/3089/htm#) in the paper) applied to raise GHG concentrations. The study involved five Yorkshire breed pigs, and their conditions were well-documented, including feeding schedules and markings for visual identification. 

The GHG concentrations were measured using gas chromatography, with carbon dioxide (CO2) being the dominant GHG. The concentrations were analyzed before, after, and one hour after treatment. The authors provided data and graphs illustrating the GHG concentrations over time.

<img src="https://github.com/supervisely/supervisely/assets/78355358/11814d89-3581-4363-a169-3921dd22653f" alt="image" width="800">

The study also included group-wise pig posture and walking behavior scores, which were assessed by counting the number of pigs exhibiting specific behaviors in each frame before, during, and after treatment. These scores revealed that pig behavior was affected by GHG levels, with increased lateral lying and reduced standing and walking activities during elevated GHG conditions.

<img src="https://github.com/supervisely/supervisely/assets/78355358/679ec616-e381-4517-9777-7685549380f5" alt="image" width="800">

Additionally, the authors presented locomotion patterns and distances traveled by walking pigs during the experiments. These observations provided insights into how GHG levels influenced pig activities throughout the day.

<img src="https://github.com/supervisely/supervisely/assets/78355358/526dc109-a609-458f-8ce9-754dae6b2a82" alt="image" width="800">

In summary, the authors conducted a comprehensive study to assess the impact of elevated GHG levels on pig behavior using computer vision and deep learning techniques. Their findings underscored the potential of this approach for non-invasive monitoring of pig health and welfare under varying environmental conditions.
