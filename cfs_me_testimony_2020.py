# -*- coding: utf-8 -*-
"""CFS/ME_Testimony_2020

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CgOb4VJqaGG2t-fR8qZqTesIw-G2EEwF

# CFS/ME Testimony (2020 Edition)

***

## GPT2-774M model, fine-tuned on all public information and papers (up to 2021) related to Chronic Fatigue Syndrome/Myalgic Encephalomyelitis

***

### Project Los Angeles

### Tegridy Code 2021

# Setup
"""

#@title Check GPU
!nvidia-smi

# Commented out IPython magic to ensure Python compatibility.
#@title Setup environment
# %tensorflow_version 1.x
!pip install -q gpt-2-simple
import gpt_2_simple as gpt2
from datetime import datetime
from google.colab import files

# Commented out IPython magic to ensure Python compatibility.
#@title Download and untar fine-tuned GPT2-774M model
# %cd /content/
!wget --no-check-certificate -O CFSMETestimony2020.tar "https://onedrive.live.com/download?cid=8A0D502FC99C608F&resid=8A0D502FC99C608F%2118467&authkey=AL4M5qofOfArnoA"
!tar -xvf /content/CFSMETestimony2020.tar

#@title Load the model
sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, run_name='CFSMETestimony')

"""# Generation"""

#@title Talk to the model

input_prompt = "What is the best possible treatment for CFS/ME? Thank you." #@param {type:"string"}
desired_length_of_output_in_tokens = 1024 #@param {type:"slider", min:8, max:1024, step:8}
creativity_temperature = 0.8 #@param {type:"slider", min:0.05, max:1, step:0.05}

gpt2.generate(sess,
              run_name='CFSMETestimony',
              top_k=64,
              length=desired_length_of_output_in_tokens,
              temperature=creativity_temperature,
              prefix=input_prompt,
              nsamples=5,
              batch_size=5
              )

"""# LICENSE

MIT License

Copyright (c) 2021 Project Los Angeles

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""