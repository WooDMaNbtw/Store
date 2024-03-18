export function convertDateToWords(dateString) {
    const months = [
        "January", "February", "March", "April", "May", "June", "July",
        "August", "September", "October", "November", "December"
    ];

    const parts = dateString.split("-");
    const year = parts[0];
    const month = months[parseInt(parts[1]) - 1];
    const day = parseInt(parts[2]);

    return `${day} ${month.toUpperCase()} ${year}`;
}
