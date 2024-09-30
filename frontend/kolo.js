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

function spinWheel() {
    if (spinning) return;
    spinning = true;
    const randomDegree = Math.floor(Math.random() * 360) + 720;
    wheel.style.transform = `rotate(${randomDegree}deg)`;
    
    setTimeout(() => {
        spinning = false;
        const selectedIndex = Math.floor(((randomDegree % 360) / 90) % 4);
        const selectedArt = artForms[selectedIndex];
        displayChallenge(selectedArt);
    }, 3000);
}

function displayChallenge(artForm) {
    const artChallenges = challenges[artForm.name];
    const randomChallenge = artChallenges[Math.floor(Math.random() * artChallenges.length)];
    
    challengeText.textContent = `Your ${artForm.name} Challenge:`;
    challenge.textContent = randomChallenge;
    challengeContainer.style.display = 'block';
}