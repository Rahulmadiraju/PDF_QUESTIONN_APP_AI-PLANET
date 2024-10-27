//frontend/src/components/Upload.js



import React, { useState } from 'react';

function Upload({ onQuestions }) {
    const [isLoading, setIsLoading] = useState(false);

    const handleFileChange = async (event) => {
        const file = event.target.files[0];
        const formData = new FormData();
        formData.append('file', file);
        setIsLoading(true);

        try {
            const response = await fetch('http://127.0.0.1:8080/upload-pdf', {
                method: 'POST',
                body: formData,
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const data = await response.json();
            onQuestions(data.questions);
        } catch (error) {
            console.error('Error:', error);
            alert('Failed to upload and process the file.');
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <div className="Upload">
            <input type="file" accept="application/pdf" onChange={handleFileChange} />
            {isLoading && <p className="processing-text">Processing PDF, please wait...</p>}
        </div>
    );
}

export default Upload;
