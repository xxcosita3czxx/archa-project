const artForms = [
    { name: 'Visual Art', icon: '🎨', color: '#FF9AA2' },
    { name: 'Music', icon: '🎵', color: '#FFB7B2' },
    { name: 'Theater', icon: '🎭', color: '#FFDAC1' },
    { name: 'Dance', icon: '💃', color: '#E2F0CB' },
];

const challenges = {
    'Visual Art': [
        "Recreate a famous painting using only emojis",
        "Draw a self-portrait using your non-dominant hand",
        "Create a collage representing your week using only magazine cutouts",
    ],
    'Music': [
        "Compose a 30-second jingle for your favorite snack",
        "Create a remix of your alarm sound",
        "Write lyrics for an existing instrumental track",
    ],
    'Theater': [
        "Perform a one-minute monologue as your favorite movie character",
        "Act out a scene from your day, but in the style of a silent film",
        "Improvise a commercial for a ridiculous product",
    ],
    'Dance': [
        "Choreograph a 15-second dance to your favorite meme song",
        "Teach a family member or friend a TikTok dance",
        "Create a dance move inspired by your pet or favorite animal",
    ],
};

const wheel = document.getElementById('wheel');
const spinButton = document.getElementById('spinButton');
const challengeContainer = document.getElementById('challengeContainer');
const challengeText = document.getElementById('challengeText');
const challenge = document.getElementById('challenge');

let spinning = false;

spinButton.addEventListener('click', spinWheel);

let currentRotation = 0;  // Keep track of the current rotation

function spinWheel() {
    if (spinning) return;
    spinning = true;

    // Generate a random degree between 720 and 1080 (2-3 full rotations)
    const randomDegree = Math.floor(Math.random() * 360) + 720;
    
    // Add the random degree to the current rotation
    currentRotation += randomDegree;
    
    // Apply the rotation to the wheel
    wheel.style.transform = `rotate(${currentRotation}deg)`;

    setTimeout(() => {
        spinning = false;

        // Calculate the final rotation within the 360-degree range
        let finalRotation = currentRotation % 360;


        while (finalRotation > 360) {
            finalRotation -= 360;
        }

        // Check the final angle with multiple if conditions
        let selectedArt;

        if (finalRotation < 90) {
            console.log("Méně než 90");
            selectedArt = artForms.find(art => art.name === 'Music'); // Music
        } 
        
        if (finalRotation >= 90 && finalRotation < 180) {
            console.log("Více než 90, ale méně než 180");
            selectedArt = artForms.find(art => art.name === 'Visual Art'); // Visual Art
        } 
        
        if (finalRotation >= 180 && finalRotation < 270) {
            console.log("Více než 180, ale méně než 270");
            selectedArt = artForms.find(art => art.name === 'Dance'); // Theater
        } 
        
        if (finalRotation >= 270 && finalRotation < 360) {
            console.log("Více než 270, ale méně než 360");
            selectedArt = artForms.find(art => art.name === 'Theater'); // Dance
        }

        // Display the selected challenge
        displayChallenge(selectedArt);
    }, 3000);  // Duration of the spin
}function displayChallenge(artForm) {
    const artChallenges = challenges[artForm.name];
    const randomChallenge = artChallenges[Math.floor(Math.random() * artChallenges.length)];
    
    challengeText.textContent = `Your ${artForm.name} Challenge:`;
    challenge.textContent = randomChallenge;
    challengeContainer.style.display = 'block';
}