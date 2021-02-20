lea     rsp, [rsp-98h]
mov     [rsp+0D0h+var_D0], rdx
mov     [rsp+0D0h+var_C8], rcx
mov     [rsp+0D0h+var_C0], rax
mov     rcx, 306Ah
call    __afl_maybe_log


v20 = _afl_prev_loc ^ a2;
_afl_prev_loc ^= v20;
_afl_prev_loc = (unsigned __int64)_afl_prev_loc >> 1;

void aaa()
{


if (strncmp(GIF_STAMP, Buf, GIF_VERSION_POS) != 0) {
    if (Error != NULL)
    *Error = D_GIF_ERR_NOT_GIF_FILE;
    (void)fclose(f);
    free((char *)Private);
    free((char *)GifFile);
    return NULL;
}


if (magicbuf[0] != (MIF_MAGIC >> 24) || magicbuf[1] != ((MIF_MAGIC >> 16) &
	  0xff) || magicbuf[2] != ((MIF_MAGIC >> 8) & 0xff) || magicbuf[3] !=
	  (MIF_MAGIC & 0xff)) {
		jas_eprintf("error: bad signature\n");
		goto error;
}

if ( !strncmp("GIFVER", Buf, 3uLL) )
        {
          v22 = (signed int)__readfsdword(0xFFFFFFFC) ^ 0x19C6LL;
          ++_afl_area_ptr[v22];
          __writefsdword(0xFFFFFFFC, 0xCE3u);


if ( magicbuf[0] != 'M' )
    goto LABEL_32;
v6 = _afl_area_ptr;
v7 = (signed int)__readfsdword(0xFFFFFFFC) ^ 0x6188LL;
++_afl_area_ptr[v7];
__writefsdword(0xFFFFFFFC, 0x30C4u);
*((_QWORD *)v6 + 0x2000) += 2100LL;
++*((_QWORD *)v6 + 8193);
if ( magicbuf[1] != 'I' )
  goto LABEL_32;
v8 = _afl_area_ptr;
v9 = (signed int)__readfsdword(0xFFFFFFFC) ^ 0xC874LL;
++_afl_area_ptr[v9];
__writefsdword(0xFFFFFFFC, 0x643Au);
*((_QWORD *)v8 + 0x2000) += 1900LL;
++*((_QWORD *)v8 + 8193);
if ( magicbuf[2] != 'F'
  || (v10 = _afl_area_ptr,
      v11 = (signed int)__readfsdword(0xFFFFFFFC) ^ 0xF871LL,
      ++_afl_area_ptr[v11],
      __writefsdword(0xFFFFFFFC, 0x7C38u),
      *((_QWORD *)v10 + 0x2000) += 1900LL,
      ++*((_QWORD *)v10 + 8193),
      magicbuf[3] != '\n') )
{
LABEL_32:
    v12 = (signed int)__readfsdword(0xFFFFFFFC) ^ 0xC411LL;
    ++_afl_area_ptr[v12];
    __writefsdword(0xFFFFFFFC, 0x6208u);
    jas_eprintf("error: bad signature\n");
    goto LABEL_26;
}

void parseconf_load_setting(const char *setting){
    while(isspace(*setting)) setting++;
    char key[128] = {0}, value[128] = {0};
    str_split(setting, key, value, '=');
    if(strlen(value) == 0){
      fprintf(stderr, "missing value in config file for : %s\n", key);
      exit(EXIT_FAILURE);
    }
}

// Skip the component keyword
	if ((id = jas_tvparser_next(tvp))) {
		// This should never happen.
		abort();
}

jas_taginfo_t *taginfo;
taginfo = taginfos;
while (taginfo->id >= 0) {
    if (!strcmp(taginfo->name, name)) {
        return taginfo;
    }
    ++taginfo;
}
return 0;

GifFileOut->SColorMap = GifMakeMapObject(
    GifFileIn->SColorMap->ColorCount,
    GifFileIn->SColorMap->Colors);
    
}

void
stackswap()
{
#ifdef DEBUG
	printf("*stackswap*\n");
#endif
	struct SWF_ACTIONPUSHPARAM *p = peek();		/* peek() includes error handling */
	char type = Stack->type;
	Stack->type = Stack->next->type;
	Stack->val  = Stack->next->val;
	Stack->next->type = type;
	Stack->next->val  = p;
}



