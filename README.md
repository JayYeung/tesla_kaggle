## Inspiration

Driving in extreme conditions like icy roads and blizzards often leads to accidents due to poor visibility or slippery surfaces. Having personally experienced car accidents caused by vehicles losing control on ice, it’s clear how critical it is to ensure that drivers are cautious and aware. Similarly, my teammates from the crowded Bay Area face challenges with complex road systems and traffic, where crashes are just as frequent. This inspired us to develop VisionGuard, a system that leverages AI to analyze driver behavior and road conditions in real-time, ultimately helping drivers make safer decisions. Our goal is to build smarter driving tools that reduce accidents and save lives.

## What it does

VisionGuard is an AI-powered system that analyzes in-car video footage in real time to transcribe and interpret driver behavior. By detecting both safe and unsafe actions, the system generates actionable insights to promote safer driving practices. VisionGuard can identify critical situations such as distracted driving, reckless maneuvers, or risky environmental conditions and alert drivers immediately. The insights provided by VisionGuard can also be used by insurance companies, fleet managers, or autonomous vehicle systems to improve road safety.

## How we built it

Computer Vision Framework: Utilized fine-tuned cutting-edge VLM's such as Gemini Pro 2.0, Pixtral with inference-time techniques including Chain of Thought, ensembling, and few-shot learning. For chain of thought, we based our prompts off of those used in OpenEMMA, an open reproduction of Waymo's EMMA project. For ensembling, we utilized a simple majority voting technique which ended up working the best. Additionally, for question-answering, we found that the model tended to be biased towards the first and last options presented (A/D), so we combatted this by shuffling the answer choices and taking the most voted options. Utilizing advanced capabilities of the VLM, we also suppose functionalities like

AI-Powered Reasoning: The system employs OpenAI’s GPT-4 API for natural language interpretation of detected behaviors. By integrating AI reasoning, VisionGuard converts detecteUtilzd patterns into meaningful feedback for the driver, such as “You seem distracted” or “Road conditions require slower speeds.”

Reinforcement Learning: We experiemented with using GRPO to fine-tune our own VLM based off the Qwen VL-2B model, which was the largest we were able to fit on the provided 4xA100 Nvidia GPUs. Our idea was to improve VLM reasoning which is important for understanding many autonomous driving scenes, in a self-reflective manner similar to DeepSeek. We utilized the TRL library from Huggingface Transformers, employing tensor sharding to deploy the VLM across multiple GPUs. We utilized the NuScenes-QA dataset with num_generations = 64 for fine-tuning, which was very similar to the Tesla-provided data. However, we were only able to fit batch_size one and after running for over 6 hours, found that our model, because of it's limited size, performed worse than existing API-based benchmarks.

## Challenges we ran into

OOM Errors: During development, we faced many out-of-memory errors due to limited VRAM when trying to run models locally, as VLMs are large and expensive to train. We ended up optimizing inference via tensor sharding, distributing the weights of a single model amoungst multiple GPUs, using DeepSpeed which barely let us fit the model on device.
Working with APIs: Many team members were beginners when it came to integrating APIs. Debugging and resolving authentication issues with third-party tools took significant effort.
Collaborative Learning Curve: Some team members were new to working with LLMs (Large Language Models), so understanding how to process video reasoning and integrate it into a real-time pipeline required significant collaboration and experimentation.

## Accomplishments that we're proud of

We’re incredibly proud of creating a functional prototype that successfully analyzes video footage to identify risky driving behaviors in real-time. This required seamlessly integrating multiple technologies—computer vision, LLMs, and reinforcement learning—despite being a relatively new domain for our team. Another highlight was how well we collaborated as a team, with everyone stepping out of their comfort zones to learn and contribute to the project. We also managed to build a pipeline that works efficiently with low-latency feedback, ensuring the driver receives timely alerts for unsafe actions.

## What we learned

This project introduced us to working with video reasoning frameworks and applying machine learning models to real-time contexts. We learned how to integrate APIs effectively and leverage AI-powered reasoning to convert raw video data into actionable insights. Additionally, we gained hands-on experience with reinforcement learning techniques, helping us understand how to train and fine-tune vision-language models for specific use cases.

## What’s next for VisionGuard: Smart Vision for Smarter Driving

Real-Time Vehicle Integration: We’d love to integrate VisionGuard into systems like Tesla Autopilot to assist drivers in real-time scenarios.
Expanded Use Cases: Beyond detecting unsafe driving behavior, VisionGuard can be extended to monitor passenger behavior (e.g., ensuring child safety) or analyze external road conditions using dashcams.
Data Partnerships: Collaborating with insurance companies and fleet management systems could help improve their risk assessments and provide discounts to safer drivers.
Advanced Environmental Awareness: Incorporating more sensors (e.g., LiDAR or GPS data) to enhance environmental context understanding, such as icy roads or sudden obstacles.

## Tech Stack:

Google Gemini, Mixtral AI (Pixtral 13B), OpenAI, HuggingFace Transformers, DeepSpeed, Torch, CUDA, OpenCV,
