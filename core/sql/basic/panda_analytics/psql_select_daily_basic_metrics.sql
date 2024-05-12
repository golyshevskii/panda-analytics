SELECT '{
  "s": "Daily metrics → May 8, 2024",
  "fontsize": 10,
  "alpha": 0.8
}'::jsonb AS        date,
       '[
         {
           "metric": {
             "s": "Сумма продаж",
             "fontsize": 8,
             "alpha": 0.7
           },
           "value": {
             "s": "457.74k",
             "fontsize": 15,
             "fontweight": "bold"
           },
           "change": {
             "s": "↓ 65%%",
             "fontsize": 7,
             "color": "red",
             "bbox": {
               "facecolor": "red",
               "edgecolor": "grey",
               "alpha": 0.15,
               "linewidth": 0.1,
               "boxstyle": "round,pad=0.6,rounding_size=1"
             }
           }
         },
         {
           "metric": {
             "s": "Количество продаж",
             "fontsize": 8,
             "alpha": 0.7
           },
           "value": {
             "s": "276",
             "fontsize": 15,
             "fontweight": "bold"
           },
           "change": {
             "s": "↓ 77%%",
             "fontsize": 7,
             "color": "red",
             "bbox": {
               "facecolor": "red",
               "edgecolor": "grey",
               "alpha": 0.15,
               "linewidth": 0.1,
               "boxstyle": "round,pad=0.6,rounding_size=1"
             }
           }
         },
         {
           "metric": {
             "s": "Сумма возвратов",
             "fontsize": 8,
             "alpha": 0.7
           },
           "value": {
             "s": "15.33k",
             "fontsize": 15,
             "fontweight": "bold"
           },
           "change": {
             "s": "↓ 25%%",
             "fontsize": 7,
             "color": "green",
             "bbox": {
               "facecolor": "green",
               "edgecolor": "grey",
               "alpha": 0.15,
               "linewidth": 0.1,
               "boxstyle": "round,pad=0.6,rounding_size=1"
             }
           }
         },
         {
           "metric": {
             "s": "Средний %% возвратов",
             "fontsize": 8,
             "alpha": 0.7
           },
           "value": {
             "s": "2.70%%",
             "fontsize": 15,
             "fontweight": "bold"
           },
           "change": {
             "s": "↓ 41%%",
             "fontsize": 7,
             "color": "green",
             "bbox": {
               "facecolor": "green",
               "edgecolor": "grey",
               "alpha": 0.15,
               "linewidth": 0.1,
               "boxstyle": "round,pad=0.6,rounding_size=1"
             }
           }
         },
         {
           "metric": {
             "s": "Логистика",
             "fontsize": 8,
             "alpha": 0.7
           },
           "value": {
             "s": "14.90k",
             "fontsize": 15,
             "fontweight": "bold"
           },
           "change": {
             "s": "↓ 28%%",
             "fontsize": 7,
             "color": "green",
             "bbox": {
               "facecolor": "green",
               "edgecolor": "grey",
               "alpha": 0.15,
               "linewidth": 0.1,
               "boxstyle": "round,pad=0.6,rounding_size=1"
             }
           }
         },
         {
           "metric": {
             "s": "Сумма штрафов",
             "fontsize": 8,
             "alpha": 0.7
           },
           "value": {
             "s": "157",
             "fontsize": 15,
             "fontweight": "bold"
           },
           "change": {
             "s": "↓ 431%%",
             "fontsize": 7,
             "color": "green",
             "bbox": {
               "facecolor": "green",
               "edgecolor": "grey",
               "alpha": 0.15,
               "linewidth": 0.1,
               "boxstyle": "round,pad=0.6,rounding_size=1"
             }
           }
         },
         {
           "metric": {
             "s": "Сумма комиссии",
             "fontsize": 8,
             "alpha": 0.7
           },
           "value": {
             "s": "95.23k",
             "fontsize": 15,
             "fontweight": "bold"
           },
           "change": {
             "s": "↓ 57%%",
             "fontsize": 7,
             "color": "green",
             "bbox": {
               "facecolor": "green",
               "edgecolor": "grey",
               "alpha": 0.15,
               "linewidth": 0.1,
               "boxstyle": "round,pad=0.6,rounding_size=1"
             }
           }
         },
         {
           "metric": {
             "s": "Средний %% комиссии",
             "fontsize": 8,
             "alpha": 0.7
           },
           "value": {
             "s": "21.50%%",
             "fontsize": 15,
             "fontweight": "bold"
           },
           "change": {
             "s": "↑ 6%%",
             "fontsize": 7,
             "color": "red",
             "bbox": {
               "facecolor": "red",
               "edgecolor": "grey",
               "alpha": 0.15,
               "linewidth": 0.1,
               "boxstyle": "round,pad=0.6,rounding_size=1"
             }
           }
         }
       ]'::jsonb AS metrics
;
