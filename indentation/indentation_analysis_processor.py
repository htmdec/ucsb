import datetime
from io import BytesIO
from openmsistream import DataFileStreamProcessor
import re 
import sys
sys.path.append("..")

class IndentationAnalysisProcessor(DataFileStreamProcessor) :
    def __init__(self,config_file,topic_name, *, out_files_dir=False,db_connection_str=None,drop_existing=False,verbose=False,**other_kwargs):
        super().__init__(config_file,topic_name,**other_kwargs)
        self.out_files_dir = out_files_dir
        #either create an engine to interact with a DB, or store the path to the output file
        self._engine = None
        self._output_file = None
        # if db_connection_str is not None :
        #     try :
        #         self._engine = create_engine(db_connection_str,echo=verbose)
        #         self._scoped_session = scoped_session(sessionmaker(bind=self._engine))
        #         self._sessions_by_thread_ident = {}
        #     except Exception as exc :
        #         errmsg = f'ERROR: failed to connect to database using connection string {db_connection_str}! '
        #         errmsg+= 'Will re-reraise original exception.'
        #         self.logger.error(errmsg,reraise=True,exc_info=exc)
        #     if drop_existing :
        #         self.logger.info(f'Dropping and recreating the {FlyerAnalysisEntry.FLYER_ANALYSIS_TABLE_NAME} table')
        #         self.__drop_existing_table()
        #         self.__create_table()
        # else :
        #     self._output_file = self._output_dir/f'{FlyerAnalysisEntry.FLYER_ANALYSIS_TABLE_NAME}.csv'
        
    def _process_downloaded_data_file(self,datafile,lock) :
        """
        Run the flyer analysis on the downloaded data file
        returns None if processing was successful, an Exception otherwise
        """
        
        r = re.compile('^..-{2}\d{8}-{2}\d{5}.txt$') # doesn't include all for now 
        if not r.match(datafile.filename):
            return None
        bytestring_data = True
        try :
            # indentation_analysis_main
            if self._output_file is not None :
                self.__write_result_to_csv(result,lock)
            elif self._engine is not None :
                self.__write_result_to_DB(result,lock)
        except Exception as exc :
            return exc
        return None

    def _on_shutdown(self):
        super()._on_shutdown()
        self._engine.dispose()

    @classmethod
    def run_from_command_line(cls,args=None) :
        """
        Run the stream-processed analysis code from the command line
        """
        #make the argument parser
        parser = cls.get_argument_parser()
        parser.add_argument('--db_connection_str',
            help='''A string to use for connecting to a database that should hold the output (SQLAlchemy format). 
                    Output will go in a .csv file if this argument is not given.''')
        parser.add_argument('--drop_existing',action='store_true',
            help='Add this flag to drop and recreate any existing table in the database on startup')
        parser.add_argument('--verbose','-v',action='store_true',
            help='Add this flag to use a verbose SQLAlchemy engine')
        parser.add_argument('--out_files_dir',help='Output of ALPSS algorithms')
        args = parser.parse_args(args=args)
        #make the stream processor
        alpss_analysis = cls(args.config,args.topic_name,
                             out_files_dir=args.out_files_dir,
                             db_connection_str=args.db_connection_str,
                             drop_existing=args.drop_existing,
                             verbose=args.verbose,
                             output_dir=args.output_dir,
                             n_threads=args.n_threads,
                             update_secs=args.update_seconds,
                             consumer_group_id=args.consumer_group_id)
        # print(alpss_analysis.out_files_dir)
        # print(alpss_analysis._output_dir)
        # exit()
        #start the processor running (returns total number of messages read, processed, and names of processed files)
        run_start = datetime.datetime.now()
        msg = f'Listening to the {args.topic_name} topic for flyer image files to analyze'
        alpss_analysis.logger.info(msg)
        n_read,n_processed,processed_filepaths = alpss_analysis.process_files_as_read()
        alpss_analysis.close()
        run_stop = datetime.datetime.now()
        #shut down when that function returns
        msg = 'Flyer analysis stream processor '
        if args.output_dir is not None :
            msg+=f'writing to {args.output_dir} '
        msg+= 'shut down'
        alpss_analysis.logger.info(msg)
        msg = f'{n_read} total messages were consumed'
        if len(processed_filepaths)>0 :
            msg+=f', {n_processed} messages were successfully processed,'
            msg+=f' and the following {len(processed_filepaths)} file'
            msg+=' ' if len(processed_filepaths)==1 else 's '
            msg+=f'had analysis results added to {args.db_connection_str}'
        else :
            msg+=f' and {n_processed} messages were successfully processed'
        msg+=f' from {run_start} to {run_stop}'
        for fn in processed_filepaths :
            msg+=f'\n\t{fn}'
        alpss_analysis.logger.info(msg)

def main(args=None) :
    ALPSStreamProcessor.run_from_command_line(args=args)

if __name__=='__main__' :
    main()