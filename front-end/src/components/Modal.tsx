import React from 'react';

interface ModalProps {
    visible: boolean;
    onClose: () => void;
    children: React.ReactNode;
}

export const Modal = ({ visible, onClose, children }: ModalProps) => {
    if (!visible) return null;

    const handleClose = (event: React.MouseEvent<HTMLDivElement>) => {
        const targetElement = event.target as HTMLDivElement;
        if (targetElement.id === "wrapper") onClose();
    }

    return (
        <>
            <div className='modal-exterior-wrapper' id='wrapper' onClick={handleClose}>
                <div className='modal-interior-wrapper'>
                    <button className='close-button' onClick={() => onClose()}>Close</button>
                    <div className='modal'>
                        {children}
                    </div>
                </div>
            </div>
        </>
    )
}