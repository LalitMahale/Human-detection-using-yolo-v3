from src.image_detection import ImageDetect
from src.video_detection import VideoDetect
import gradio as gr

def main_process(choice, image_input=None, video_input=None):
    if choice == "Image" and image_input is not None:
        output_image = ImageDetect().image_detection(image_path=image_input)
        return output_image, None
    elif choice == "Video" and video_input is not None:
        output_video = VideoDetect().videodetection(video_path=video_input)
        return None, output_video
    else:
        return None, None  # No valid input provided

def update_inputs(choice):
    if choice == "Image":
        return True, False  # Show image input, hide video input
    else:
        return False, True  # Hide image input, show video input

with gr.Blocks() as iface:
    choice = gr.Radio(["Image", "Video"], label="Choose Input Type", value="Image")
    
    image_input = gr.Image(type="numpy", label="Upload Image", visible=True)
    video_input = gr.Video(label="Upload Video", visible=False)

    output_image = gr.Image(type="numpy", label="Output Image")
    output_video = gr.Video(label="Processed Video")
    
    process_button = gr.Button("Process")

    choice.change(update_inputs, inputs=choice, outputs=[image_input, video_input])

    process_button.click(
        main_process,
        inputs=[choice, image_input, video_input],
        outputs=[output_image, output_video]
    )

iface.launch(share=True, server_port=8888)
