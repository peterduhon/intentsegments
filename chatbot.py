import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pandas as pd

nltk.download('punkt')
nltk.download('stopwords')

class SegmentationChatbot:
    def __init__(self, segments_file=None):
        if segments_file:
            self.segments = pd.read_csv(segments_file)
        else:
            self.segments = pd.DataFrame({'segment': [0, 1, 2, 0, 1, 2]})
        self.stop_words = set(stopwords.words('english'))
        self.segment_names = {0: "Low Engagement", 1: "Moderate Engagement", 2: "High Engagement"}
        self.targeting_advice = {
            "Low Engagement": "Focus on re-engagement campaigns and basic brand awareness.",
            "Moderate Engagement": "Offer personalized content and product recommendations to increase engagement.",
            "High Engagement": "Prioritize for high-value offers and loyalty programs."
        }

    def process_input(self, user_input):
        tokens = word_tokenize(user_input.lower())
        tokens = [w for w in tokens if w not in self.stop_words]
        
        if 'segment' in tokens or 'segments' in tokens:
            return self.provide_segment_info()
        elif 'name' in tokens or 'names' in tokens:
            return self.provide_segment_names()
        elif 'target' in tokens or 'targeting' in tokens:
            return self.provide_targeting_advice()
        else:
            return "I'm sorry, I don't understand. You can ask me about segments, their names, or targeting advice."

    def provide_segment_info(self):
        segment_counts = self.segments['segment'].value_counts()
        info = f"There are {len(segment_counts)} segments. The distribution is:\n"
        for segment, count in segment_counts.items():
            info += f"{self.segment_names[segment]}: {count} users\n"
        return info

    def provide_segment_names(self):
        return "The segment names are: " + ", ".join(self.segment_names.values())

    def provide_targeting_advice(self):
        advice = "Here's how you should target each segment:\n"
        for name, targeting in self.targeting_advice.items():
            advice += f"{name}: {targeting}\n"
        return advice

if __name__ == '__main__':
    chatbot = SegmentationChatbot('user_segments_with_time.csv')
    print("Ask me about user segments (type 'exit' to quit):")
    while True:
        user_input = input("> ")
        if user_input.lower() == 'exit':
            break
        response = chatbot.process_input(user_input)
        print(response)