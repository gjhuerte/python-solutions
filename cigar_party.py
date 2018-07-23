#cigar party
def cigar_party(cigars, is_weekend):
	if is_weekend == True:
		return (cigars >= 40)
	else:
		return (cigars >= 40) and (cigars <= 60)
