from transformers import pipeline

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import BoxLayout
from transformers import pipeline
modal=pipeline("sentiment-analysis")

class MainApp(MDApp):
    def build(self):
        print("Building the app interface...")
        # Initialize the sentiment analysis model
        self.model = pipeline("sentiment-analysis")
        print("Model loaded successfully.")

        # Create a vertical layout
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Create a text field for input
        self.text_field = MDTextField(
            hint_text="Enter text here",
            size_hint=(1, None),
            height=30
        )
        self.layout.add_widget(self.text_field)

        # Create a submit button
        self.button = MDRaisedButton(
            text="Analyze Sentiment",
            pos_hint={'center_x': 0.5},
            on_release=self.analyze_sentiment
        )
        self.layout.add_widget(self.button)

        # Create a label to display results
        self.result_label = MDLabel(
            text="",
            halign='center'
        )
        self.layout.add_widget(self.result_label)

        return self.layout

    def analyze_sentiment(self, instance):
        print("Analyzing sentiment...")
        text = self.text_field.text.strip()
        if text:
            try:
                result = self.model(text)[0]
                self.result_label.text = f"Label: {result['label']}, Confidence: {result['score']:.2f}"
                print("Analysis complete.")
            except Exception as e:
                self.result_label.text = f"Error processing text: {str(e)}"
                print(f"Error: {str(e)}")
        else:
            self.result_label.text = "Please enter some text for analysis."
            print("No text entered.")

if __name__ == '__main__':
    MainApp().run()
