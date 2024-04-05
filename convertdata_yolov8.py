#this scipt is used to convert yolov8 format

import cv2
import os
import re

classes = ['Bowl','CanOfCocaCola', 'MilkBottle', 'Mug']

def normalize_bbox(bbox, img_width, img_height):
    x, y, width, height = bbox

    # Calculate bounding box center coordinates
    x_center = (x + width / 2) / img_width
    y_center = (y + height / 2) / img_height

    # Calculate bounding box width and height
    box_width = width / img_width
    box_height = height / img_height

    return x_center, y_center, box_width, box_height


def saveframe(frame ,classid, yolo_img_path,frame_no, place_no, subject_no):
    file_name =  f"frame{classes[classid]}_{frame_no}_place{place_no}_subject{subject_no}.jpg"
    file_path = os.path.join(yolo_img_path, file_name)

    # Save the frame as an image file
    cv2.imwrite(file_path, frame)

def savetxt(classid ,frame,frame_no,bbox,annotation_path,place_no, subject_no):
    frame_height, frame_width, _ = frame.shape  # Get frame dimensions
    # Normalize bounding box coordinates
    x_center, y_center, box_width, box_height = normalize_bbox(bbox, frame_width, frame_height)
    # Create filename
    file_name = f"frame{classes[classid]}_{frame_no}_place{place_no}_subject{subject_no}.txt"
    file_path = os.path.join(annotation_path, file_name)
    # Write to text file (create new file each time)
    with open(file_path, 'w') as f:
        f.write(f"{classid} {x_center} {y_center} {box_width} {box_height}")


def read_frame():
    pass

def visualize_image(frame, bbox):
    x, y, w, h = bbox  # Unpack bbox
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)  # Green color, thickness=2
    return frame


def main(path_to_images, path_to_boundingbox,place_no, subject_no ,yolo_img_path,annotation_path ,classid,Visualize_img = True):

    #read the path
    images_folder_path = os.listdir(path_to_images)
    #print(images_folder_path)


    frame_no = 0
    with open(path_to_boundingbox, 'r') as file:
        lines = file.readlines()

    for line in lines:
        parts = line.split()
        frame_name = parts[0]
        bbox = list(map(int, parts[1:]))
        # x, y, w, h = bbox

        for img_file in images_folder_path:
            #new_filename = filename.replace("_fg", "")
            if img_file == frame_name:
                image_path = os.path.join(path_to_images, img_file)
                frame = cv2.imread(image_path)
                saveframe(frame, classid, yolo_img_path, frame_no, place_no, subject_no)
                savetxt(classid, frame, frame_no, bbox, annotation_path, place_no, subject_no)
                if Visualize_img is True:
                    frame = visualize_image(frame, bbox)
                    cv2.imshow('Bounding Box', frame)
                    cv2.waitKey(122)

                frame_no = frame_no + 1

def run_main(path_for_class,bbpath, yolo_img_path, annotation_path, class_id):
    path_for_dirs = os.listdir(path_for_class)
    print(path_for_dirs)
    for path in path_for_dirs:
        extracted_frames_1 = os.path.join(path_for_class,path)

        place_number_match = re.search(r'Place(\d+)', extracted_frames_1)
        place_number = place_number_match.group(1) if place_number_match else None

        # Extract subject number using regular expression
        subject_number_match = re.search(r'Subject(\d+)', extracted_frames_1)
        subject_number = subject_number_match.group(1) if subject_number_match else None

        extracted_frames = extracted_frames_1 + "\extract_frame"
        bounding_box_path = f"{bbpath}/{path}/bounding_box_new.txt"
        main(extracted_frames, bounding_box_path, place_number, subject_number, yolo_img_path, annotation_path, class_id, Visualize_img=True)

if __name__ == '__main__':
    #path_to_images = r"C:\Users\rohin\Desktop\New folder (2)\trdp\datasets\MilkBottle\MilkBottle\MilkBottlePlace7Subject3\extract_frame"
    path_to_images = r"C:\Users\rohin\Desktop\New folder (2)\trdp\datasets\Mug\Mug"
    bounding_box_path = r"C:\Users\rohin\Desktop\New folder (2)\trdp\datasets\BoundingBoxes\BoundingBoxes\Mug"

    yolo_img_path = r"C:\Users\rohin\Desktop\New folder (2)\trdp\datasets\yolov8_format\images"
    annotation_path = r"C:\Users\rohin\Desktop\New folder (2)\trdp\datasets\yolov8_format\annotations"
    classid = 3
    #main(path_to_images, bounding_box_path, 7, 3, yolo_img_path, annotation_path, classid, Visualize_img=True)

    run_main(path_to_images,bounding_box_path, yolo_img_path, annotation_path, class_id=classid)

    # bounding_box_path =r"C:\Users\rohin\Desktop\New folder (2)\trdp\datasets\BoundingBoxes\BoundingBoxes\MilkBottle\MilkBottlePlace7Subject3\bounding_box_new.txt"
