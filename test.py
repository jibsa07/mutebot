import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '/')

@client.event
async def on_ready():
    print('Online')



@client.command()
@commands.has_any_role('😆관리자😆', '🥶봇🥶', 676660972072468501)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention}')

@client.command()
@commands.has_any_role('😆관리자😆', '🥶봇🥶', 676660972072468501)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f' banned {member.mention}')

@client.command()
@commands.has_any_role('😆관리자😆', '🥶봇🥶', 676660972072468501)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

@client.command()
@commands.has_any_role('😆관리자😆', '🥶봇🥶', 676660972072468501)
async def mute(ctx, member : discord.Member):
    guild = ctx.guild

    for role in guild.roles:
        if role.name == "Muted":
            await member.add_roles(role)
            await ctx.send("{} has {} has been muted" .format(member.mention,ctx.author.mention))
            return
            
            Overwrite = discord.PermissionOverwrite(send_message=False)
            newRole = await guild.create_role(name="Muted")

            for channel in guild.text_channels:
                await channel.set_permissions(newRole,Overwrite=Overwrite)

            await member.add_roles(newRole)
            await ctx.send("{} has {} has been muted" .format(member.mention,ctx.author.mention))


@client.command()
@commands.has_any_role('😆관리자😆', '🥶봇🥶', 676660972072468501)
async def unmute(ctx, member : discord.Member):
    guild = ctx.guild
    
    for role in guild.roles:
        if role.name == "Muted":
            await member.remove_roles(role)
            await ctx.send("{} has {} has been unmuted" .format(member.mention,ctx.author.mention))
            return







client.run('NjkzNDAzMjk1NDY4NzQ4ODAw.Xn8kMQ.rxxMcXkoYQKMnp-r2jxnbJYwfdk')
#NjkzNDAzMjk1NDY4NzQ4ODAw.Xn8kMQ.rxxMcXkoYQKMnp-r2jxnbJYwfdk