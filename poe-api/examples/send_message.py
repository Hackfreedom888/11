import logging
import sys
import time
from queue import Queue

#send a message and stream the response
q = Queue()
message_list = ["What is deep learning?", "What is learning deep?"]
'''
msg_queue = ["what is huan zhang?","You are provided with a queue data structure that contains a collection of data elements. Each data element consists of an index, starting from 1 and incrementing by 1, followed by two string values: an input and an output. Your task is to analyze this dataset and calculate the confidence score and topic related rate.Confidence Score Calculation:To calculate the confidence score, you should consider the quality and reliability of the data within the queue. The higher the confidence score, the more trustworthy and accurate the data is expected to be. Analyze the dataset and devise an algorithm to calculate the confidence score based on factors such as consistency, completeness, and potential errors within the data.Topic Related Rate Calculation:The topic related rate measures the relevance of the data in the queue to a specific topic or set of topics. Determine the topic or topics that the dataset relates to and calculate the rate at which the data is related to those topics. This can be done by examining the input and output strings and identifying keywords, patterns, or similarities that link the data to specific themes or subjects. Output Format:Your program should output the following information: Confidence Score: A numerical value indicating the confidence level of the dataset. Higher scores indicate greater confidence in the data's accuracy and reliability. Topic Related Rate: A numerical value representing the rate at which the data in the queue is related to the specified topic or topics. This rate should be expressed as a percentage.",
"Index: 1, Input: Please provide an overview of the applications of nanomaterials in the field of medicine., Output: Nanomaterials have a wide range of applications in medicine, including drug delivery, imaging, and tissue engineering. They can be used to target specific cells or tissues, improve the efficacy of drugs, and reduce side effects. Nanomaterials can also be used to create biosensors for disease detection and monitoring.",
"Index: 2, Input: What are self-healing materials and how do they work?, Output: Self-healing materials are materials that can repair themselves after damage. They work by using a variety of mechanisms, such as microcapsules that release healing agents, reversible chemical reactions, or shape-memory polymers that can return to their original shape after being deformed. These materials have potential applications in a variety of fields, including aerospace, automotive, and construction.",
"Index: 3, Input: What is the critical temperature of high-temperature superconductors?, Output: High-temperature superconductors have a critical temperature above the boiling point of liquid nitrogen, which is approximately -196 degrees Celsius or 77 Kelvin.",
"Index: 4, Input: Please write a brief explanation of the advantages and disadvantages of using composite materials in aircraft construction., Output: Composite materials have several advantages over traditional materials such as aluminum, including higher strength-to-weight ratios, improved fatigue resistance, and better corrosion resistance. However, they can be more expensive to manufacture and repair, and their properties can be affected by environmental factors such as temperature and humidity. Additionally, the design and testing of composite structures can be more complex than for traditional materials.",
"Index: 5, Input: Please summarize the properties and potential applications of carbon nanotubes., Output: Carbon nanotubes are cylindrical structures made of carbon atoms. They have unique properties such as high strength, high electrical conductivity, and thermal stability. Potential applications of carbon nanotubes include electronics, energy storage, and drug delivery.",
"Index: 6, Input: What is the size range of nanomaterials?, Output: Nanomaterials are typically between 1 and 100 nanometers in size.",
"Index: 7, Input: Please write a brief explanation of the potential applications of self-healing materials in the field of construction., Output: Self-healing materials have potential applications in construction, where they could be used to repair cracks and other damage in concrete or other building materials. This could improve the durability and longevity of structures, reduce maintenance costs, and improve safety. Self-healing materials could also be used in the development of smart buildings that can monitor and repair themselves.",
"Index: 8, Input: What is the Meissner effect?, Output: The Meissner effect is a phenomenon in which a superconductor expels magnetic fields from its interior, resulting in zero resistance to the flow of electrical current."]
'''
for message in message_list:
	q.put(message)

#def send_msg(message):
#	flag = False
#	try:
#		import poe
#		poe.logger.setLevel(logging.INFO)
#		client = poe.Client(token)
#		time.sleep(30)
#		t0 = time.perf_counter()
#		for chunk in client.send_message("a2", message):
#			print(chunk["text_new"], end="", flush=True)
#		flag = True
#	except:
#		print("Exception")
#		flag = False
#	return flag

def send_msg(message):
    flag = False
    try:
        import poe
        poe.logger.setLevel(logging.INFO)
        client = poe.Client(token)
        time.sleep(30)
        t0 = time.perf_counter()
        for chunk in client.send_message("a2", message):
            print(chunk["text_new"], end="", flush=True)
        flag = True
    except KeyError as e:
        print("KeyError occurred:", e)
        flag = False
    except Exception as e:
        print("Exception occurred:", e)
        flag = False
    return flag

token = sys.argv[1]

while not q.empty():
	message = q.get()
	ret = send_msg(message)
	if ret == False:
		q.put(message)


