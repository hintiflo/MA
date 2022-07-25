// modBoundInt


	if( !isFull(ptr) )
	{
		while( !isFull(ptr) )
			append(ptr, getItem() )
	}else
	{
		blockItems();
	}
	
	while( isValid(ptr) )	// outer loop
	{	
		ptr++;
		
		for(idx = 0; idx < 4; idx++) // inner loop
		{	
			itm[idx] = decomposeItem(ptr, idx);
		}
		
		processItem( itm[3], itm[2], itm[1], itm[0]);
	}

	free(ptr);	