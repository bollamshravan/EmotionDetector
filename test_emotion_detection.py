from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detection():
        test_cases = [
            ("I am glad this happened", "joy"),
            ("I am really mad about this", "anger"),
            ("I feel disgusted just hearing about this", "disgust"),
            ("I am so sad about this", "sadness"),
            ("I am really afraid that this will happen", "fear")
        ]

        for statement, expected_dominant_emotion in test_cases:
            result = emotion_detector(statement)
            assert result['dominant_emotion'] == expected_dominant_emotion, f"Failed for statement: {statement}"

if __name__ == "__main__":
    test_emotion_detection()
    print("All tests passed!")