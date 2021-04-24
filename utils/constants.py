RAW_DATA_DIR = "raw_data/"
RAW_FEATURES = ["activityType", "aerobicTrainingEffect", "anaerobicTrainingEffect", "avgHr", "avgSpeed", "calories",
                "distance", "maxDoubleCadence", "maxFtp", "maxHr", "maxSpeed"]
FILTERED_FEATURES = ['running', 'strength_training', 'indoor_cardio', 'mountain_biking', 'hiking',
                     'trail_running', 'cycling', 'other']
ACTIVITIES_MAP = {
    'running': 0,
    'biking': 1,
    'indoor_cardio': 2,
    'strength_training': 3,
    'hiking': 4,
    'other': 5
}
