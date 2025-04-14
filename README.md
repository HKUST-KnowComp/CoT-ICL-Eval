## *The Curse of CoT*: <br> On the Limitations of Chain-of-Thought in In-Context Learning

Official Github repository for the benchmark datasets and codes in the paper: <br>
*The Curse of CoT: On the Limitations of Chain-of-Thought in In-Context Learning* ([arXiv:2504.05081](https://arxiv.org/abs/2504.05081)).


## Datasets

| Dataset | Source Paper | Task Modality | Size |
|---------|-------|-------------|-----------------|
|ARC|[On the Measure of Intelligence](https://arxiv.org/pdf/1911.01547)|Symbolic|835|
|MiniARC|[Playgrounds for Abstraction and Reasoning](https://openreview.net/pdf?id=F4RNpByoqP)|Symbolic|149|
|1D-ARC|[LLMs and the Abstraction and Reasoning Corpus: Successes, Failures, and the Importance of Object-based Representations](https://arxiv.org/pdf/2305.18354)|Symbolic|901|
|SCAN|[Generalization without Systematicity: On the Compositional Skills of Sequence-to-Sequence Recurrent Networks](https://arxiv.org/pdf/1711.00350v3)|Textual|1000|
|MiniSCAN|[Learning Compositional Rules via Neural Program Synthesis](https://arxiv.org/pdf/2003.05562)|Textual|1000|
|COGS|[COGS: A Compositional Generalization Challenge Based on Semantic Interpretation](https://arxiv.org/pdf/2010.05465)|Textual|1000|
|SALT|[LogiDynamics: Unraveling the Dynamics of Logical Inference in Large Language Model Reasoning](https://arxiv.org/pdf/2502.11176)|Textual|1200|
|List Functions|[The child as hacker: building more human-like models of learning](https://dspace.mit.edu/handle/1721.1/129232)|Numerical|1250|
|RAVEN|[In-Context Analogical Reasoning with Pre-Trained Language Models](https://aclanthology.org/2023.acl-long.109.pdf)|Numerical / Symbolic|1259|


## Citation

If you find our paper interesting, please cite our paper:

```bibtex
@misc{zheng2025cursecotlimitationschainofthought,
      title={The Curse of CoT: On the Limitations of Chain-of-Thought in In-Context Learning}, 
      author={Tianshi Zheng and Yixiang Chen and Chengxi Li and Chunyang Li and Qing Zong and Haochen Shi and Baixuan Xu and Yangqiu Song and Ginny Y. Wong and Simon See},
      year={2025},
      eprint={2504.05081},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2504.05081}, 
}
