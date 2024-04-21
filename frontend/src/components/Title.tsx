import axios from 'axios'
import React, { useState } from 'react'


interface Props{
    setMessages: any,
    setColor: any
}
export function Title({setMessages, setColor}: Props) {

    const [isResetting, setIsResetting] = useState(false);

    async function resetConversation(){
        setIsResetting(true);

        await axios.get('http://localhost:8000/reset')
                .then(function(response) {

                if (response.status === 200) {

                    setMessages([])
                    setIsResetting(false)

                } else {

                    console.log("There was an error api request");
                }

            }).catch(function(error) {
                console.log(error)
                alert("There was an error resetting the conversation")
            })

        setIsResetting(false);
    }


  return (
    // <div className='flex flex-row justify-between items-center w-full p-4 bg-gray-900 text-white font-bold shadow'>
    <div className={`flex flex-row justify-between items-center w-full p-4 text-white font-bold shadow ${setColor}`}>
        <div className='italic'>Nova</div>

        <button
        onClick={resetConversation}
        className={
          "transition-all duration-300 text-blue-300 hover:text-pink-500 " +
          (isResetting && "animate-pulse")
        }
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          strokeWidth={1.5}
          stroke="currentColor"
          className="w-6 h-6"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            d="M16.023 9.348h4.992v-.001M2.985 19.644v-4.992m0 0h4.992m-4.993 0l3.181 3.183a8.25 8.25 0 0013.803-3.7M4.031 9.865a8.25 8.25 0 0113.803-3.7l3.181 3.182m0-4.991v4.99"
          />
        </svg>
      </button>
        
    </div>
  )
}
