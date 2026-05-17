--- eda.ipynb ---

Explores the dataset (EVOreal_time_synth.csv) used in this project. Checks data shape, missing values,
participant records, feature distributions.

--- build_subject_files.py ---

Splits the dataset (EVOreal_time_synth.csv) into one CSV file per participant, sorted by Timestamp, to 
preserve temporal order. Outputs 53 files to data/subjects/.

--- split_data.py ---

Shuffles and splits (by copying) the files in data/subjects/ into training, validation and testing sets. Ouputs 37 files to /data/train/,
8 files to /data/val/ and 8 files to /data/test/.

--- task_1/raw_features_class.py --- 

Trains and evaluates logistic regression, random forest and gradient boosting using all acoustic features in the data to predict "SoundClass".

--- task_2/impute_hvol.py ---

Fills missing hVol values for each participant using the last observation carried forward (LOCF). Missing hVol
means the participant did not change the hearing aid volume, so the device keeps the previous setting.
Reads from data/subjects/, outputs imputed files to data/subjects_imputed/.

--- task_2/build_daily_features.py ---

Builds daily feature summaries per participant. Reads from data/subjects_imputed/, outputs data/daily_features.csv
(one row per participant per day).

--- task_2/aggregate_participants.py ---

Aggregates daily features to one row per participant (mean across all days).
Reads from data/daily_features.csv, outputs data/participant_daily_profile.csv.

--- task_2/feature_selection.py ---

Drops one feature from each correlated pair (|r| > 0.75) to remove redundant features before clustering.
Reads from data/participant_daily_profile.csv, outputs data/participant_profiles_selected.csv.

--- task_2/normalization.py ---

Provides a normalize_features() function that applies StandardScaler (z-score normalization) to the
feature columns of dataframe. Returns the normalized dataframe and the fitted scaler.

--- task_2/clustering_algorithms.py ---

K-Means clustering functions: evaluate k values (elbow method and silhouette score) and fit a final model.

--- task_2/run_clustering.py ---

Runs K-Means clustering on participant profiles: finds the best k, fits a final model, validates cluster
stability with leave-one-out cross-validation, and checks whether clusters reflect real differences in hearing loss.

--- task_2/build_weekly_features.py ---

Aggregates daily features to weekly summaries per participant.
Reads from data/daily_features.csv, outputs data/weekly_features.csv (one row per participant per week).

--- task_2/dtw_clustering.py ---

DTW-based clustering functions: evaluates k values (elbow and silhouette), fits a final DTW k-means model,
and runs agglomerative hierarchical clustering using a precomputed DTW distance matrix.

--- task_2/run_trajectory_clustering.py ---

Runs trajectory clustering on weekly behavioral profiles: finds the best k, fits DTW k-means and hierarchical
clustering models, plots weekly trajectories per cluster, generates a t-SNE projection, and checks cluster
differences in hearing loss (PTA4).

--- task_2/build_daily_features_2.py ---

Extends build_daily_features.py with daily mean acoustic environment features. Reads from data/subjects_imputed/, outputs data/daily_features_2.csv.

--- task_2/run_mixed_effects.py ---

Mixed-effects regression to see if daily acoustic conditions predict hearing aid usage time. Reads from data/daily_features_2.csv.
