# Facial Keypoints Detection: Detection the location of keypoints on face images:

The objective of this task is to predict keypoint positions on face images. This can be used as a building block in several applications, such as:

* tracking faces in images and video;
* analysing facial expressions;
* detecting dysmorphic facial signs for medical diagnosis;
* biometrics / face recognition.

Detecing facial keypoints is a very challenging problem.  Facial features vary greatly from one individual to another, and even for a single individual, there is a large amount of variation due to 3D pose, size, position, viewing angle, and illumination conditions. Computer vision research has come a long way in addressing these difficulties, but there remain many opportunities for improvement.

The data set for this competition was graciously provided by [**Dr. Yoshua Bengio**](http://www.iro.umontreal.ca/~bengioy/yoshua_en/index.html) of the University of Montreal.

## Training and testing data:

Each predicted keypoint is specified by an (x,y) real-valued pair in the space of pixel indices. There are 15 keypoints, which represent the following elements of the face:

* left_eye_center;
* right_eye_center;
* left_eye_inner_corner;
* left_eye_outer_corner;
* right_eye_inner_corner;
* right_eye_outer_corner;
* left_eyebrow_inner_end;
* left_eyebrow_outer_end;
* right_eyebrow_inner_end;
* right_eyebrow_outer_end;
* nose_tip;
* mouth_left_corner;
* mouth_right_corner;
* mouth_center_top_lip;
* mouth_center_bottom_lip.

Left and right here refers to the point of view of the subject.

In some examples, some of the target keypoint positions are misssing (encoded as missing entries in the csv, i.e., with nothing between two commas).

The input image is given in the last field of the data files, and consists of a list of pixels (ordered by row), as integers in (0,255). The images are 96x96 pixels.

### Main data files:

* **training.csv**: list of training 7049 images. Each row contains the *(x,y)* coordinates for 15 keypoints, and image data as row-ordered list of pixels;
* **test.csv**: list of 1783 test images. Each row contains ImageId and image data as row-ordered list of pixels;
* **submissionFileFormat.csv**: list of 27124 keypoints to predict. Each row contains a RowId, ImageId, FeatureName, Location. FeatureName are "left_eye_center_x," "right_eyebrow_outer_end_y," etc. Location is what you need to predict. 

You can access data files [here](https://www.kaggle.com/c/facial-keypoints-detection/data).

Those files mentioned above are large sized files; so, none of **training.csv**, **test.csv**, and their zipped forms is not here, since it is not possible to upload the files with larger size than 100.0 Mb. But it does not mean we are helpless. No!

### Updated data files:

* **intro.py**: this python script takes .csv formatted files **training.csv** and **test.csv** which are extracted from **training.zip**, **test.zip**, and parses into different matrices:
  * **trainData.csv**: list of training 7049 images without 15 keypoints. It is just images vs. whole 96x96 coordinates. Since the size is large, it is not here;
  * **testData.csv**: list of 1783 test images. Each row contains ImageId and image data as row-ordered list of pixels. Since the size is large, it is not here;
  * **LabelName.csv**: the list of names for keypoints;
  * **trainLabel.csv**: list of labels for 7049 training images. They are just *(x, y)* coordinates for 15 keypoints.
* **data_to_img.py**: this python script takes **trainData.csv** and **testData.csv**, and can display and save any picture from them. From which data to choose, which picture in the data to choose, which color you want for background are depending on your choices; so, yes, this is interactive script.

The only things left for you to do are just to download *.zip* files from [here](https://www.kaggle.com/c/facial-keypoints-detection/data), extract *.csv* files out of them, run **intro.py** and **data_to_img.py**.

Thanks for your time!
