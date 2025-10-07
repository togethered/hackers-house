document.addEventListener('DOMContentLoaded', () => {
    const door = document.querySelector('.door');
    const doorLink = document.querySelector('.door-link');

    let isDoorOpen = false;
    let isAnimating = false;

    const openDoor = (e) => {
        if (isAnimating) return;

        isAnimating = true;
        isDoorOpen = true;
        door.classList.add('is-open');

        // Prevent multiple clicks during animation
        door.removeEventListener('click', openDoor);

        // Redirect after animation completes
        setTimeout(() => {
            if (doorLink && doorLink.href) {
                window.location.href = doorLink.href;
            }
        }, 1000); // Match CSS transition duration
    };

    if (door) {
        door.addEventListener('click', openDoor);
    }

    // Prevent default link behavior until after animation
    if (doorLink) {
        doorLink.addEventListener('click', (e) => {
            e.preventDefault();
            if (!isDoorOpen) {
                openDoor(e);
            }
        });
    }
});