import cv2
import os
import re


def make_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory '{directory}' created successfully.")
    else:
        print(f"Directory '{directory}' already exists.")

    return directory

def save_frame(vid_path , savepath):

    cap = cv2.VideoCapture(vid_path)

    # Variable to keep track of the frame number
    frame_number = 0

    # Loop through the video frames
    while True:
        # Read a frame from the video
        ret, frame = cap.read()

        # If frame is not read properly, break the loop
        if ret:
            # Save the frame with the corresponding filename
            filename = f'Frame_{frame_number}.png'
            # saving_dir =r"C:\Users\rohin\Desktop\New folder (2)\trdp\datasets\MilkBottle\MilkBottle\MilkBottlePlace1Subject1\extract_frame/"
            saving_dir = savepath +"/"
            cv2.imwrite(saving_dir + filename, frame)

            # Increment frame number
            frame_number += 40  # Assuming the video has a constant frame rate and you want to save every 40th frame

            # Move to the next frame
            #cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
        else:
            break

    # Release the video capture object and close the window
    cap.release()
    cv2.destroyAllWindows()


def visualize_frame(bounding_box_path,extract_frame,saving_path):
    # Path to the directory containing images
    image_dir = extract_frame

    image_filenames = os.listdir(image_dir)
    print(image_filenames)

    # original_image_width = 1920
    # original_image_height = 1080

    # Path to the text file containing bounding box information
    bbox_file = bounding_box_path

    with open(bbox_file, 'r') as file:
        lines = file.readlines()
    bounding_boxes = {}
    for line in lines:
        parts = line.split()
        frame_name = parts[0]
        bbox = list(map(int, parts[1:]))
        x, y, w, h = bbox

        for filename in image_filenames:
            # new_filename = filename.replace("_fg", "")
            if filename == frame_name:
                image_path = os.path.join(image_dir, filename)
                frame = cv2.imread(image_path)

                # width_scale = original_image_width / frame.shape[1]
                # height_scale = original_image_height / frame.shape[0]

                # Scale bounding box coordinates
                x = int(x)
                y = int(y)
                w = int(w)
                h = int(h)

                print(x, y, w, h)
                frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                filename = f'Frame_{frame_name}.png'  # Use frame_name instead of frame_number
                # cv2.imshow("frame",frame)
                # cv2.waitKey(1)
                saving_dir = saving_path + "/"
                cv2.imwrite(os.path.join(saving_dir, filename), frame)
                # cv2.imshow('Bounding Box', frame)
                # cv2.waitKey(122)


def get_paths(path_for_class,bbpath):
    path_for_dirs = os.listdir(path_for_class)
    for path in path_for_dirs:
        fullpath = os.path.join(path_for_class, path)
        # Extract place number using regular expression
        place_number_match = re.search(r'Place(\d+)', fullpath)
        place_number = place_number_match.group(1) if place_number_match else None

        # Extract subject number using regular expression
        subject_number_match = re.search(r'Subject(\d+)', fullpath)
        subject_number = subject_number_match.group(1) if subject_number_match else None

        extractpath = fullpath + "/extract_frame"
        make_dir(extractpath)
        save_frame(f"{fullpath}/{path}.mp4",extractpath)
        #save_frame(f"C:/Users/rohin/Desktop/New folder (2)/trdp/datasets/MilkBottle/MilkBottle/MilkBottlePlace{place_number}Subject{subject_number}\MilkBottlePlace{place_number}Subject{subject_number}.mp4", extractpath)
        visualizepath = fullpath + "/visualize_frames"
        make_dir(visualizepath)

        bounding_box_path =f"{bbpath}/{path}/bounding_box_new.txt"
        visualize_frame(bounding_box_path, extractpath, visualizepath)
        print(f"progress for {path} is finished!")







if __name__ == '__main__':
    path_for_class = r"C:\Users\rohin\Desktop\New folder (2)\trdp\datasets\Mug\Mug"
    bounding_box_path = r"C:\Users\rohin\Desktop\New folder (2)\trdp\datasets\BoundingBoxes\BoundingBoxes\Mug"
    get_paths(path_for_class,bounding_box_path)



    # extractpath = path_for_class + "/extract_frame"
    # make_dir(extractpath)
    # save_frame(r"C:\Users\rohin\Desktop\New folder (2)\trdp\datasets\MilkBottle\MilkBottle\MilkBottlePlace7Subject3\MilkBottlePlace7Subject3.mp4" , extractpath)
    # visualizepath = path_for_class + "/visualize_frames"
    # make_dir(visualizepath)
    # bounding_box_path = r"C:\Users\rohin\Desktop\New folder (2)\trdp\datasets\BoundingBoxes\BoundingBoxes\MilkBottle\MilkBottlePlace7Subject3\bounding_box_new.txt"
    # visualize_frame(bounding_box_path,extractpath, visualizepath)



































