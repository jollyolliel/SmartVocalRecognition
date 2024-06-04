
## Smart Vocal Recognition

This is a basic smart vocal recognition program written in Python.

### Features:

-   **Speech Recognition:** Uses Google Speech-to-Text to convert spoken words to text.
-   **Text-to-Speech:** Uses the pyttsx3 library to convert text to speech for user interaction.
-   **Youtube Search:** Opens Youtube searches based on user voice commands.
-   **Joke Teller:** Tells jokes using the pyjokes library.
-   **Shutdown:** Shuts down the computer after a 5-second countdown (**Warning:** Use with caution, data loss may occur).

### Dependencies:

The program requires the following Python libraries:

-   pyttsx3
-   speech_recognition
-   webbrowser (for Youtube search)
-   pyjokes (for joke telling)
-   os (for shutdown)

You can install these libraries using the `pip` command:

Bash

```
pip install pyttsx3 speech_recognition webbrowser pyjokes os

```

### Usage:

1.  Save the code as a Python file (e.g.,  `smart_vocal_recognition.py`).
2.  Run the script from your terminal:

Bash

```
python smart_vocal_recognition.py

```

Use code with caution.

3.  The program will start listening for your voice commands.

### Base Recognition File (for reference):

The `Base recognition file` included in the code is a simpler version that only listens for user input and speaks it back. This demonstrates the core functionality of speech recognition and text-to-speech.

### Additional Notes:

-   This is a basic example and can be extended with additional functionalities.
-   The program currently uses a 5-second countdown before shutting down. Make sure to save your work before running the shutdown command.
