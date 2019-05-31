
def notowords(number):
	i=0
	no=""
	word=""
	while i<len(number):
		if i==0 and len(number)>3:
			if ord(number[i])==57:
				no+="nine thousand "
			else:
				if ord(number[i])==56:
					no+="eight thousand "
				else:
					if ord(number[i])==55:
						no+="seven thousand "
					else:
						if ord(number[i])==54:
							no+="six thousand "
						else:
							if ord(number[i])==53:
								no+="five thousand "
							else:
								if ord(number[i])==52:
									no+="four thousand "
								else:
									if ord(number[i])==51:
										no+="three thousand "
									else:
										if ord(number[i])==50:
											no+="two thousand "
										else:
											if ord(number[i])==49:
												no+="one thousand "

		else:
			if i==1 and len(number)==4 or i ==0 and len(number)==3:
				if ord(number[i])==57:
					no+="nine hundred "
				else:
					if ord(number[i])==56:
						no+="eight hundred "
					else:
						if ord(number[i])==55:
							no+="seven hundred "
						else:
							if ord(number[i])==54:
								no+="six hundred "
							else:
								if ord(number[i])==53:
									no+="five hundred "
								else:
									if ord(number[i])==52:
										no+="four hundred "
									else:
										if ord(number[i])==51:
											no+="three hundred "
										else:
											if ord(number[i])==50:
												no+="two hundred "
											else:
												if ord(number[i])==49:
													no+="one hundred "
			else:
				if i==2 and len(number)>3 or i==1 and len(number)>2 or i==0 and len(number)>1:
					if ord(number[i])==57:
						no+="ninety "
					else:
						if ord(number[i])==56:
								no+="eighty "
						else:
							if ord(number[i])==55:
								no+="seventy "
							else:
								if ord(number[i])==54:
									no+="sixty "
								else:
									if ord(number[i])==53:
										no+="fivety "
									else:
										if ord(number[i])==52:
											no+="fourty "
										else:
											if ord(number[i])==51:
												no+="thirty "
											else:
												if ord(number[i])==50:
													no+="twenty "
												else:
													if ord(number[i])==49 and ord(number[i+1])==48:
														no+="ten"
													else:
														if ord(number[i])==49 and ord(number[i+1])==49:
															no+="eleven"
														else:
															if ord(number[i])==49 and ord(number[i+1])==50:
																no+="twelve"
															else:
																if ord(number[i])==49 and ord(number[i+1])==51:
																	no+="thirteen"
																else:
																	if ord(number[i])==49 and ord(number[i+1])==52:
																		no+="fourteen"
																	else:
																		if ord(number[i])==49 and ord(number[i+1])==53:
																			no+="fifteen"
																		else:
																			if ord(number[i])==49 and ord(number[i+1])==54:
																				no+="sixteen"
																			else:
																				if ord(number[i])==49 and ord(number[i+1])==55:
																					no+="seventeen"
																				else:
																					if ord(number[i])==49 and ord(number[i+1])==56:
																						no+="eighteen"
																					else:
																						if ord(number[i])==49 and ord(number[i+1])==57:
																							no+="nineteen"
				else:
					if i==0 and len(number)<2 or i==1 and len(number)==2 or i==2 and len(number)==3 or i==3 and len(number)==4:
						if ord(number[i])==57:
							no+="nine"
						else:
							if ord(number[i])==56:
								no+="eight"
							else:
								if ord(number[i])==55:
									no+="seven"
								else:
									if ord(number[i])==54:
										no+="six"
									else:
										if ord(number[i])==53:
											no+="five"
										else:
											if ord(number[i])==52:
												no+="four"
											else:
												if ord(number[i])==51:
													no+="three"
												else:
													if ord(number[i])==50:
														no+="two"
													else:
														if ord(number[i])==49:
															no+="one"			
		i+=1
	print(no)

msg=input("enter your number here:")

notowords(msg)






