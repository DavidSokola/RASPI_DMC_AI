import torch

# Load TorchScript model
torchscript_model = torch.jit.load('/home/david/DMC/yolov5/best.torchscript')
torchscript_model.eval()

# Dummy input tensor matching your model's input size
dummy_input = torch.randn(1, 3, 640, 640)  # Adjust size (3, 640, 640) if needed

# ONNX export path
onnx_path = '/home/david/DMC/yolov5/best.onnx'

# Export to ONNX
torch.onnx.export(
    torchscript_model,          # TorchScript model
    dummy_input,                # Input tensor
    onnx_path,                  # Path to save ONNX model
    input_names=['input'],      # Input name
    output_names=['output'],    # Output name
    opset_version=11            # ONNX opset version (11 is widely supported)
)

print(f"ONNX model exported to {onnx_path}")
