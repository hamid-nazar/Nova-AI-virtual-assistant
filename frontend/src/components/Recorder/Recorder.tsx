import React, { useState } from "react";


import "./Recorder.css";
import { RecordIcon } from "../RecordIcon";
import { MessagRecorder} from "../MessagRecorder";
import axios from "axios";
import { Title } from "../Title";



export function Recorder() {

  const [isLoading, setIsLoading] = useState(false)
  const [messages, setMessages] = useState<any[]>([])
  let blob = new Blob();

  function createBlobURL(data: any) {

    const blob = new Blob([data], { type: "audio/mpeg" });

    const url = window.URL.createObjectURL(blob);

    return url;
  }

  async function handleStop(blobUrl: string) {

    setIsLoading(true)

    try {


      const myMessage = { sender: "me", blobUrl };
      const messagesArr = [...messages, myMessage];

      const response = await fetch(blobUrl);
      const blob = await response.blob();
      const formData = new FormData();
      formData.append('file', blob, 'myFile.wav');


      const res = await axios.post('http://localhost:8000/audio', formData,
        {
          headers:
          {
            'Access-Control-Allow-Origin': '*',
            "Content-Type": "audio/mpeg",
          },
          responseType: "arraybuffer"
        })

      const adamMessage = { sender: "adam", blobUrl: createBlobURL(res.data) }

      // messagesArr.push(adamMessage)

      // setMessages(messagesArr)

      // console.log(messages.length)

      const audio = new Audio(adamMessage.blobUrl);

      setIsLoading(false)

      if(response.status === 200){

        audio.play();
      }
    

    } catch (error) {

      console.log(error)

      setIsLoading(false)
    }


  }



  return (
    <>
    <Title setMessages={setMessages} setColor={"bg-gray-500 "}/>
    <div className="main">
      
      <div className="image-container">
        <div className="image">
          <img src="robot.gif" alt="image"  className="rounded-full"/>
        </div>
        <h1>Nova</h1>
        <p>I'm your virtual assistant Nova. How may I help you?</p>
      </div>
      <div className="input cursor-pointer">
        <button className="talk">
          
          <MessagRecorder handleStop={handleStop} />
          </button>
        <h1 className="content">{isLoading ? "Loading..." :" Click here to speak"}</h1>
      </div>
    </div>
    </>
  );
}
