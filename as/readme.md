Scripts are expecting the scraped HTML files to be in these folders:

		* "/data/utexas/"
		* "/data/texas_bar/"

Remove the helpers and unindent the main block to compensate:
		
		* "hellpaz":
			+ Loge (Dumps the error into a trio of loggers; JSON, Run History, Last Run Only)
			+ LoggingPrinter (Saves everything printed to console in a textfile)
