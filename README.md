## Diff-Privacy

PyTorch Code for "Diff-Privacy: Diffusion-based Face Privacy Protection" (Accepted by TCSVT)


## Getting Started

### Prerequisites

  For packages, see environment.yaml.

  ```sh
  conda env create -f environment.yaml
  conda activate ldm
  ```

### Train:
  Train MSI:
   ```sh
   python main.py --base configs/stable-diffusion/v1-finetune.yaml
               -t 
               --actual_resume ./models/sd/sd-v1-4.ckpt
               -n <run_name> 
               --gpus 0, 
               --data_root /path/to/directory/with/images
               --lightning
   ```
   
   See `configs/stable-diffusion/v1-finetune.yaml` for more options.

   Download the pretrained [Stable Diffusion Model](https://huggingface.co/CompVis/stable-diffusion-v-1-4-original/resolve/main/sd-v1-4.ckpt) and save it at ./models/sd/sd-v1-4.ckpt.

   Download the pretrained [FaceNet](https://objects.githubusercontent.com/github-production-release-asset-2e65be/188506754/fcf96f80-becd-11ea-8462-de7c2385f193?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20230926%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230926T092506Z&X-Amz-Expires=300&X-Amz-Signature=0bcc8de7db1783656b7249bb06c8016a43c74fd0ae9efdb67deac38836df06f7&X-Amz-SignedHeaders=host&actor_id=109660296&key_id=0&repo_id=188506754&response-content-disposition=attachment%3B%20filename%3D20180402-114759-vggface2.pt&response-content-type=application%2Foctet-stream) and [ArcFace](https://ml.cs.tsinghua.edu.cn/~xiaoyang/face_models/ArcFace/model_ir_se50.pth).

### Inference: 

  According to your needs, run `Anonymization.ipynb` or `Visual identity information hiding.ipynb` to obtain encrypted images. Then run `Identity_recover.ipynb` to obtain the decrypted image. 


### Acknowledgments

  * This code builds heavily on **[InST](https://github.com/zyxElsa/InST)**. Thanks for open-sourcing!
