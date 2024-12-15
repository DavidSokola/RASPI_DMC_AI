
    Train your model:
    Once the docker is started, you can start training your model.
        Prepare your custom dataset - Follow the steps described here in order to create:
            dataset.yaml configuration file
            Labels - each image should have labels in YOLO format with corresponding txt file for each image.
            Make sure to include number of classes field in the yaml, for example: nc: 80
        Start training - The following command is an example for training a yolov5s model.

        python train.py --img 640 --batch 16 --epochs 3 --data coco128.yaml --weights yolov5s.pt --cfg models/yolov5s.yaml

            yolov5s.pt - pretrained weights. You can find the pretrained weights for yolov5s, yolov5m, yolov5l, yolov5x and yolov5m_wo_spp in your working directory.
            models/yolov5s.yaml - configuration file of the yolov5 variant you would like to train. In order to change the number of classes make sure you update this file.
        NOTE: We recommend to use yolov5m_wo_spp for best performance on Hailo-8
    Export to ONNX:
    In order to export your trained YOLOv5 model to ONNX run the following script:

    python models/export.py --weights /path/to/trained/model.pt --img 640 --batch 1  # export at 640x640 with batch size 1

