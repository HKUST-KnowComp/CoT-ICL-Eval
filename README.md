## *The Curse of CoT*: <br> On the Limitations of Chain-of-Thought in In-Context Learning

Official Github repository for the benchmark datasets and codes in the paper: <br>
*The Curse of CoT: On the Limitations of Chain-of-Thought in In-Context Learning* ([arXiv:2504.05081](https://arxiv.org/abs/2504.05081)).

## Main Results*

*Results averaged across 16 Large Language Models.

| Dataset       | Direct Answering | CoT    | CoT tokens | React  | React tokens | ToT    | ToT tokens |
|---------------|------------------|--------|------------|--------|--------------|--------|------------|
| ARC           | **10.01**            | 7.50   | 914.04     | 6.34   | 955.76       | 6.99   | 1376.96    |
| MiniARC       | **17.11**           | 10.36  | 419.75     | 8.69   | 663.37       | 8.85   | 233.47     |
| 1DARC         | **41.30**            | 34.93  | 359.57     | 28.51  | 435.97       | 27.88  | 594.70     |
| SCAN          | **62.79**            | 60.04  | 134.51     | 57.35  | 270.16       | 51.31  | 455.39     |
| MiniSCAN      | **20.85**            | 17.32  | 239.99     | 15.72  | 330.14       | 15.42  | 554.62     |
| COGS          | **19.73**            | 14.88  | 244.11     | 12.99  | 272.18       | 9.24   | 484.92     |
| SALT          | **37.72**            | 34.15  | 175.99     | 31.06  | 316.41       | 27.25  | 492.73     |
| List Function | **44.31**            | 38.29  | 305.49     | 34.84  | 310.73       | 31.25  | 486.49     |
| RAVEN         | **16.94**            | 7.37   | 434.75     | 3.09   | 533.09       | 5.80   | 737.64     |
| **Average**       | **30.08**            | 24.98  | 358.69     | 22.07  | 454.20       | 20.44  | 601.88     |

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
