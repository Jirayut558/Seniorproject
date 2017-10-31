'''from gensim.models import Word2Vec
import deepcut
a = ['ฉันรักภาษาไทยเพราะฉันเป็นคนไทยและฉันเป็นคนไทย' ,'ฉันเป็นนักเรียนที่ชื่นชอบวิทยาศาสตร์และเทคโนโลยี' ,'ฉันไม่ใช่โปรแกรมเมอร์เพราะฉันทำมากกว่าคิดเขียนพัฒนาโปรแกรมทดสอบโปรแกรม','ฉันชื่นชอบวิทยาศาสตร์ชอบค้นคว้าตั้งสมมุติฐานและหาคำตอบ']
b = [list(deepcut.tokenize(i)) for i in a] # ทำการตัดคำแล้วเก็บใน list จะได้เป็น [['ฉัน',...],['ฉัน',...]...]
print(b)
model = Word2Vec(b, min_count=1)
aa=model.most_similar("รัก")
print(aa)
'''

import gensim
model = gensim.models.Word2Vec.load("education.th.model")
vec = (model.wv['ควย'])
print(vec,vec[0])
