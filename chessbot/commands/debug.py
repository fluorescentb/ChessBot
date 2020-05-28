from chessbot.command import *

class CommandDebug(Command):
    name = "debug"
    help_string = "Debug command for developers"
    aliases = ["debug", "await"]
    level = LEVEL_OWNER

    @classmethod
    async def run(self,ctx):
        user = ctx.user
        guild = ctx.guild
        ch = ctx.ch
        msg = ctx.msg
        dbguild = ctx.dbguild
        game = ctx.game
 
        if ctx.command == "debug":
            try:
                o = eval(ctx.content.replace(ctx.prefix+ctx.command+" ",""))
                await ctx.ch.send(codeblock(o))
            except Exception as E:
                await ctx.ch.send(codeblock(traceback.format_exc()))

        elif ctx.command == "await":
            try:
                o = await eval(ctx.content.replace(ctx.prefix+ctx.command+" ",""))
                await ctx.ch.send(codeblock(o))
            except Exception as E:
                await ctx.ch.send(codeblock(traceback.format_exc()))