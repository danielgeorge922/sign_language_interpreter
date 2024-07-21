import React, { useEffect, useRef } from 'react';

const VideoFeed: React.FC<{ isLocal: boolean }> = ({ isLocal }) => {
  const videoRef = useRef<HTMLVideoElement>(null);

  useEffect(() => {
    if (isLocal) {
      navigator.mediaDevices.getUserMedia({ video: true })
        .then(stream => {
          if (videoRef.current) {
            videoRef.current.srcObject = stream;
          }
        })
        .catch(err => console.error('Error accessing webcam:', err));
    }
  }, [isLocal]);

  return <video ref={videoRef} autoPlay className="video-feed" style={{ width: '100%', borderRadius: '8px' }} />;
};

export default VideoFeed;
