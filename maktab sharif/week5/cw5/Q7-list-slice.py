sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
slicer = len(sample_list) // 3
chunk1 = sample_list[:slicer]
chunk2 = sample_list[slicer:slicer*2]
chunk3 = sample_list[slicer*2:]
print(f"chunk1: {chunk1}\nAfter reversing it {chunk1[::-1]}\n\nchunk2: {chunk2}\nAfter reversing it"
      f" {chunk2[::-1]}\n\nchunk3: {chunk3}\nAfter reversing it {chunk3[::-1]}")