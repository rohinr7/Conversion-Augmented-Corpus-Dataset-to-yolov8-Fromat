# Conversion-Augmented-Corpus-Dataset-to-yolov8-Fromat
Annotations are collected from Gaze information from TOBI glass2

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>How to Run the Script</title>
</head>
<body>
    <h1>How to Run the Script</h1>
    <p>This guide will help you run the Python script designed for extracting frames from a video and visualizing bounding boxes on those frames.</p>
    
    <h2>Prerequisites</h2>
    <ul>
        <li>Python installed on your machine.</li>
        <li>OpenCV library installed. You can install it using <code>pip install opencv-python-headless</code>.</li>
        <li>A video file from which you want to extract frames.</li>
        <li>A text file containing bounding box coordinates.</li>
    </ul>
    
    <h2>Steps to Run the Script</h2>
    <ol>
        <li>Place your video file and bounding box text file in an accessible directory.</li>
        <li>Open the script using a text editor or an IDE of your choice.</li>
        <li>Modify the script paths (video path, bounding box path, etc.) to match your file locations.</li>
        <li>Open a terminal or command prompt.</li>
        <li>Navigate to the directory containing the script.</li>
        <li>Run the script by typing <code>python script_name.py</code>, replacing <code>script_name.py</code> with the name of your script file.</li>
        <li>The script will create directories for extracted frames and visualized frames, and it will process the video and bounding box data accordingly.</li>
    </ol>
    
    <h2>Understanding the Output</h2>
    <p>After running the script, you will find two new directories containing the extracted frames and the visualized frames. The visualized frames will include bounding boxes drawn over the objects of interest as specified in your bounding box file.</p>
</body>
</html>
