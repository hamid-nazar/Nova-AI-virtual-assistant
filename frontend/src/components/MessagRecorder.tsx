import React from 'react'
import { RecordIcon } from './RecordIcon';
import { ReactMediaRecorder } from 'react-media-recorder';

interface props{
  handleStop(blobUrl: string): void;
}
export function MessagRecorder({handleStop}: props) {


  return (
      <ReactMediaRecorder audio onStop={handleStop}
      render={({status, startRecording, stopRecording, }) =>
       <div className='mt-2'>
        <button onMouseDown={startRecording} onMouseUp={stopRecording} className='mb-3 p-4 w-full rounded-full flex justify-between'>
          <RecordIcon classText={status=="recording" ? "animate-pulse text-red-500":"text-sky-500"}/>
        </button>
        {/* <p>{status}</p> */}
      </div> }
      />
  )
}
