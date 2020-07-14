text = "X-DSPAM-Confidence:    0.8475";
npos = text.find("0")
slice= text[npos:]
fslice = float(slice)
print(fslice)