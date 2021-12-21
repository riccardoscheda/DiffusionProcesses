# DiffusionProcesses
In This project i will try to analyze diffusion processes beginning from 
a Monte Carlo simulation the Langevin equation to obtain the statistical
 properties of the system and to obtain a probability density function
 rho(x,t). Then using the rho(x,t) the entropy of the system is computed.  

# Usage with conda
Create a new conda environment:
```
conda create -n dif_proc python=3.6
```
```
conda activate dif_proc
```
```
pip install -r requirements.txt
```
Then you can run the code with:
```
python main.py
```