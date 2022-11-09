const Discord = require("discord.js");

const { prefix, token } = require("./config.json");

const client = new Discord.Client({
    intents: [
        Discord.Intents.FLAGS.GUILDS,
        Discord.Intents.FLAGS.GUILD_MESSAGES,
        Discord.Intents.FLAGS.DIRECT_MESSAGES
    ]
});



client.once("ready", () => {
    console.log("I am ready bro");

});

client.on('message', (message) => {
    if (message.content === prefix + "ping") {
        message.reply("Okay okay");
    }
    else
        if (message.content === prefix + "info") {
            message.channel.send(
                `**Nom du serveur :** ${message.guild.name}\n**Nombre de membres :** ${message.guild.memberCount}`
            )
        }
        else {
            message.channel.send(message);
        }
});

client.on('ctx', (message, texte) => {

    if (message.content === prefix + "say") {
        if (message.author.bot){
            return;
        }
         else {
            message.channel.send(message);
        }   
        
    }
});

client.login(token);